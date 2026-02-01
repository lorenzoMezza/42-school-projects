#ifndef RUSH02_H
# define RUSH02_H
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>

//Dimensione MASSima per ogni lettira su un file e semi arbitraria non a cazzo
# define BUFFER_SIZE 4096


/**
	FUNZIONISOLO DIZIONARIO
**/
// Struttura del dizionario
typedef struct s_dict
{
	char	*key;
	char	*value;
}	t_dict;

// Funzione per parsing
t_dict	*ft_parse_dict(char *filename, int *size);
// Funzione per liberare il dizionario
void	ft_free_dict(t_dict *dict, int size);
// Funzione per prendere un valore dal dizionario
char	*ft_get_value(t_dict *dict, int size, char *key);

/**
	FUNZIONI DI UTILITA
**/

// Dtaa la size di una stringa
int		ft_strlen(char *str);
//scrive una stringa
void	ft_putstr(char *str);
// Restituisce una nuova stringa duplicata da str prima
char	*ft_strdup(char *str);
// cmpara le 2s stringhe torna 0 se sono uguali carattere per carattere
int		ft_strcmp(char *s1, char *s2);
// Verifica se il carattere e uno spazio
int		ft_is_space(char c);
// Rimuve spazi ed caratteri bianch a l'inizio e alla fine della stringa
char	*ft_trim(char *str);
//verifica se la stringa contiene solo caratteri numerici
int		ft_is_numeric(char *str);
//xontrolla che tutta la stringa sia un numero valido
int		ft_is_valid_number(char *str);
//stampa un mesagio di errore
void	ft_print_error(char *msg);

#endif
