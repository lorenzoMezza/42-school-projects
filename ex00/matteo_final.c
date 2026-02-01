#include <stdlib.h>
#include "rush02.h"

/*
 * one_and_nzero: crea e stampa una stringa tipo "1000", "1000000", ecc.
 * nzero è il numero di zeri da aggiungere dopo l'1
 * ritorna il nuovo valore di nzero decrementato di 3
 */
int	one_and_nzero(int nzero, t_dict *dict, int dictSize)
{
	int		i;
	char	*str;
	
	if (nzero < 3)
		return (nzero);
	
	str = (char *)malloc(nzero + 2); 
	if (!str)
		return (nzero);
	
	str[0] = '1';
	i = 1;
	while (i <= nzero)
	{
		str[i] = '0';
		i++;
	}
	str[i] = '\0';
	
	ft_putstr(" ");
	ft_putstr(ft_get_value(dict, dictSize, str));
	ft_putstr(" ");
	free(str);
	return (nzero - 3);
}

int	substring1(char *str, int start, t_dict *dict, int dictSize)
{
	char	sub_str[2];
	
	// Copia 1 carattere
	sub_str[0] = str[start];
	sub_str[1] = '\0';
	
	check_1(sub_str, dict, dictSize);
	return (1);
}

int	substring2(char *str, int start, t_dict *dict, int dictSize)
{
	char	sub_str[3];
	
	// Copia 2 caratteri
	sub_str[0] = str[start];
	sub_str[1] = str[start + 1];
	sub_str[2] = '\0';
	
	check_2(sub_str, dict, dictSize);
	return (2);
}

int	substring3(char *str, int start, t_dict *dict, int dictSize)
{
	char	sub_str[4];
	
	// Copia 3 caratteri
	sub_str[0] = str[start];
	sub_str[1] = str[start + 1];
	sub_str[2] = str[start + 2];
	sub_str[3] = '\0';
	
	check_3(sub_str, dict, dictSize);
	return (3);
}


int	is_all_zeros(char *str, int len)
{
	int i;
	
	i = 0;
	while (i < len && str[i])
	{
		if (str[i] != '0')
			return (0);
		i++;
	}
	return (1);
}

/*
 * Processa la stringa dividendola in chunk di 1, 2 o 3 cifre
 * e stampando i corrispondenti moltiplicatori (thousand, million, ecc.)
 */
int	str_start(char *str, t_dict *dict, int dictSize)
{
	int		str_len;
	int		i_str;
	int		nzero;
	int		chunk_len;
	
	str_len = ft_strlen(str);
	i_str = 0;
	nzero = ((str_len - 1) / 3) * 3;
	
	
	if ((str_len % 3) == 1)
	{
		chunk_len = 1;
		if (!is_all_zeros(str + i_str, chunk_len))
		{
			i_str += substring1(str, i_str, dict, dictSize);
			nzero = one_and_nzero(nzero, dict, dictSize);
		}
		else
		{
			i_str += 1;
			nzero -= 3;
		}
	}
	else if ((str_len % 3) == 2)
	{
		chunk_len = 2;
		if (!is_all_zeros(str + i_str, chunk_len))
		{
			i_str += substring2(str, i_str, dict, dictSize);
			nzero = one_and_nzero(nzero, dict, dictSize);
		}
		else
		{
			i_str += 2;
			nzero -= 3;
		}
	}
	
	while (i_str < str_len)
	{
		if (!is_all_zeros(str + i_str, 3))
		{
			i_str += substring3(str, i_str, dict, dictSize);
			nzero = one_and_nzero(nzero, dict, dictSize);
		}
		else
		{
			i_str += 3;
			nzero -= 3;
		}
	}
	
	ft_putstr("\n");
	return (0);
}
