#ifndef RUSH02_H
# define RUSH02_H

# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>



//dimenzione massima per ogni lettura su un file e semi arbitraria
# define BUFFER_SIZE 4096


/**
	FUNZIONI DIZIONARIO
**/

//Struttura del dizionario
typedef struct s_dict
{
	char	*key;
	char	*value;
}	t_dict;

// Funzione per parsing
t_dict	*ft_parse_dict(char *filename, int *size);

//funzione per liberare il dizionriio
void	ft_free_dict(t_dict *dict, int size);

// Dunzione per prendere un valore dal dizionario
char	*ft_get_value(t_dict *dict, int size, char *key);



/**
	FUNZIONI DI UTILITA
**/

//restituisce una nuova stringa duplicata da str
char	*ft_strdup(char *str);

// Rimuove spazi ed caratteri bianchi all'inizio e alla fine della stringa
char	*ft_trim(char *str);

// Virifica se la stringa contiene solo caratteri numerici
int		ft_is_numeric(char *str);






#endif
