#ifndef RUSH02_H
# define RUSH02_H
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>
#include <stdio.h>
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

void	check_3(char *str , t_dict *dict, int dictSize);
void	check_2(char *str, t_dict *dict, int dictSize);
void	check_1(char *str, t_dict *dict, int dictSize);
char *ft_substr(char *s, unsigned int start, size_t len);
int	str_start(char *str, t_dict *dict, int dictSize);
/**
	FUNZIONI DI UTILITA
**/
int	error_argn(int argn);
char	*error_arg(char **argv);
char	*is_number_valid(char *str);
int	is_number_valid_edge_case(char *dummy);
void	finalize_check2(char *str, t_dict *dict, int dictSize);
void	continua_check_3(char *str, t_dict *dict, int dictSize);
int	one_and_nzero(int nzero, t_dict *dict, int dictSize);
int	substring1(char *str, int start, t_dict *dict, int dictSize);
int	substring2(char *str, int start, t_dict *dict, int dictSize);
int	substring3(char *str, int start, t_dict *dict, int dictSize);
int	str_start(char *str, t_dict *dict, int dictSize);
char	*ft_append_read(int fd, char *content);
int	ft_count_lines(char *content);
char	*ft_create_line(char *content, int start, int end);
char *char_to_string(char charac);
char	*ft_strcat(char *dest, char *src);
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
