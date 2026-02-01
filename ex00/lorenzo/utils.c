#include "rush02.h"

/*
	SEMPLICI FUNZIONI DI UTILITAS PER LAVORARE IN MODO SEMPLICE CN LE STRINGGHE
*/

//DA LA size di un astirnga
int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}


//scrive un carattere
void	ft_putstr(char *str)
{
	write(1, str, ft_strlen(str));
}


//restituisce una nuova stringa duplicata da str
char	*ft_strdup(char *str)
{
	char	*dup;
	int		i;

	dup = malloc(ft_strlen(str) + 1);
	if (!dup)
		return (NULL);
	i = 0;
	while (str[i])
	{
		dup[i] = str[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}


//comprara le 2 stirnghe torna 0 se sono uugauli craatter eper carattere
int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] && s2[i] && s1[i] == s2[i])
		i++;
	return (s1[i] - s2[i]);
}


//verifica se e il carattere e uno spazio
int	ft_is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n' || c == '\r');
}


// togliespazi ed caratteri bianchi all'inizio e alla fine della stringa
char	*ft_trim(char *str)
{
	int		start;
	int		end;
	int		i;
	char	*trimmed;

	start = 0;
	while (str[start] && ft_is_space(str[start]))
		start++;
	end = ft_strlen(str) - 1;
	while (end >= start && ft_is_space(str[end]))
		end--;
	trimmed = malloc(end - start + 2);
	if (!trimmed)
		return (NULL);
	i = 0;
	while (start <= end)
		trimmed[i++] = str[start++];
	trimmed[i] = '\0';
	return (trimmed);
}

//controlla che una stringa e una cifra ritorna 0 se vero
int	ft_is_numeric(char *str)
{
	int	i;

	i = 0;
	if (!str || !str[0])
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}


//controlla che tutta la stringa sia un numero valido ritorna 
// 1 se lo e e zero se non lo e o e vuota
int	ft_is_valid_number(char *str)
{
	int	i;

	if (!str || !str[0])
		return (0);
	i = 0;
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

//giusto per non fare sempre i write questa si occupa di ritornare un messagio
void	ft_print_error(char *msg)
{
	w(msg);
}
