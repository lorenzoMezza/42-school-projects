#include "rush02.h"

char	*ft_read_file(char *filename)
{
	int		fileDescriptor; //numero che il sistema operativo usa per identificare quel file aperto
	int		bytes_read;
	char	buffer[BUFFER_SIZE + 1]; // +1 per \o
	char	*content; //contenuto conmpleto finale
	char	*temp;
	int		total_size; //tagli totale del file
	int		i;
	int		j;

	fileDescriptor = open(filename, O_RDONLY);
	if (fileDescriptor == -1)
		return (NULL);
	content = malloc(1);
	if (!content)
		return (NULL);
	content[0] = '\0';
	total_size = 0;
	while ((bytes_read = read(fileDescriptor, buffer, BUFFER_SIZE)) > 0) //0 significa che e arrivato a fine file -1 erorre sopra 0 indica i byte letti dal file
	{
		buffer[bytes_read] = '\0';
		temp = malloc(total_size + bytes_read + 1);
		if (!temp)
		{
			free(content);
			close(fileDescriptor);
			return (NULL);
		}
		i = 0;
		while (i < total_size)
		{
			temp[i] = content[i];
			i++;
		}
		j = 0;
		while (j < bytes_read)
		{
			temp[i + j] = buffer[j];
			j++;
		}
		temp[i + j] = '\0';
		free(content);
		content = temp;
		total_size += bytes_read;
	}
	if (bytes_read == -1)
	{
		free(content);
		close(fileDescriptor);
		return (NULL);
	}
	close(fileDescriptor);
	return (content);
}

char	**ft_split_lines(char *content, int *line_count)
{
	char	**lines;
	int		count;
	int		i;
	int		j;
	int		k;
	int		start;

	count = 1;
	i = 0;
	while (content[i])
	{
		if (content[i] == '\n')
			count++;
		i++;
	}
	lines = malloc(sizeof(char *) * (count + 1));//crea per la size del linee
	if (!lines)
		return (NULL);
	i = 0;
	j = 0;
	start = 0;
	while (content[i])
	{
		if (content[i] == '\n')
		{
			lines[j] = malloc(i - start + 1);
			if (!lines[j])
				return (NULL);
			k = 0;
			while (start < i)
				lines[j][k++] = content[start++];
			lines[j][k] = '\0';
			j++;
			start = i + 1;
		}
		i++;
	}
	if (start < i)
	{
		lines[j] = malloc(i - start + 1);
		k = 0;
		while (start < i)
			lines[j][k++] = content[start++];
		lines[j][k] = '\0';
		j++;
	}
	lines[j] = NULL;
	*line_count = j;
	return (lines);
}


// questa qui analizza una riga del dizionario nel formato < numero : testo > del cazzo e, se è valida, riempie una struttura t_dict, ritorna 0 se tutto andato bene -1 se c'e un erroe e 1 se la riga non e valida per il formato speicficato dall subject
int	ft_parse_line(char *line, t_dict *entry)
{
	int		i;
	int		colon_pos;
	char	*key_part;
	char	*value_part;

	i = 0;
	colon_pos = -1;
	while (line[i])
	{
		if (line[i] == ':')
		{
			colon_pos = i;
			break;
		}
		i++;
	}
	if (colon_pos == -1)
		return (0);
	key_part = malloc(colon_pos + 1);
	if (!key_part)
		return (-1);
	i = 0;
	while (i < colon_pos)
	{
		key_part[i] = line[i];
		i++;
	}
	key_part[i] = '\0';
	value_part = ft_strdup(line + colon_pos + 1);//sposto il puntatore di lines
	if (!value_part)
	{
		free(key_part);
		return (-1);
	}
	entry->key = ft_trim(key_part); // ho usato -> perche key nel dict e un puntator enon un valore quindi non posso fare entry.key = ma dovre fare *(entry.key) = quindi -> e la stessa cos ama shortcut
	entry->value = ft_trim(value_part);
	free(key_part);
	free(value_part);
	if (!entry->key || !entry->value || !ft_is_numeric(entry->key))//verifihiamo che il malloc fatto da ft_trim non abbia fallito e se La chiave NON è un numero in questo caso la righa e invalida 
	{
		if (entry->key)
			free(entry->key);
		if (entry->value)
			free(entry->value);
		return (0);
	}
	return (1);
}


//Questo parsa un file file e lo interpreta come da regole pe run dizionare e lo straforma in una struttara data array di dict che port aogni chiave valore facile da accedere
//se C'e un problema con il file come non esiste o pure e in formato sabgliato torna null, ritorna nulla anche se malloc da problemi.
//in sintesi alla fine riotrna una array di t_dict e ogni t_dict contiene una coppia chiavi valore
t_dict	*ft_parse_dict(char *filename, int *size)

{
	char	*content;
	char	**lines;
	t_dict	*dict;
	int		line_count;
	int		i;
	int		j;
	int		result;

	content = ft_read_file(filename);
	if (!content)
		return (NULL);
	lines = ft_split_lines(content, &line_count); //QUESTO si prende il contenuto completo del file e lo divide un un **array char dove ogni stringa e una linea e scrive dentro lincount il nuemro di linee totali puo servire si vedra
	free(content);//come disse mia nonna quando il forno si ruppe.. sono sempre i migliori ad andarsene. Per mio nonno non lo aveva detto pero.
	if (!lines)
		return (NULL);
	dict = malloc(sizeof(t_dict) * line_count); //ora sappiamo quanto deve essere grand eil dizionario quindi lo inizializziamo 
	if (!dict)
		return (NULL);
	i = 0;
	j = 0;
	while (i < line_count && j < DICT_SIZE)
	{
		result = ft_parse_line(lines[i], &dict[j]);
		if (result == -1)//errore malloc 
		{
			ft_free_dict(dict, j);
			return (NULL);
		}
		if (result == 1)//se e una riga valida aumenta j che e la size finale del dizionario
			j++;
		i++;
	}
	*size = j;
	i = 0;
	while (lines[i])//liberiamo ogni linea tanto ora non serve piu abbiamo creato il nostro dizionario e li ci sta tutto
		free(lines[i++]);
	free(lines);
	return (dict);//FINALMENTE SI RITONA L'OGETTO RISULTATNTE DALLA TRAFORMAZIONE DEL FILE
}
//Funizone per liberare completamente un dizionario 
void	ft_free_dict(t_dict *dict, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (dict[i].key)
			free(dict[i].key);
		if (dict[i].value)
			free(dict[i].value);
		i++;
	}
	free(dict);
}
