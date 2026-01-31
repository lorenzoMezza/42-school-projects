/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   matteo_workplace.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 15:00:38 by mbrunial          #+#    #+#             */
/*   Updated: 2026/01/31 18:46:09 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

ft_strlen(char *str);

check_3(char *str, int triplette_len);

char	*one_and_nzero(int nzero)
{
	int		i_str;
	char	*str;

	nzero += 2;
	str = (char *)malloc(nzero);
	i_str = 0;
	str[i_str] = '1';
	str++;
	while (i_str < nzero)
	{
		str[i_str] = '0';
		i_str++;
	}
	str[i_str] = '\0';
	return (str);
}

/*
 * nzero is magic formula don't touch
 funzione non testata
 */
int	str_start(char *str)
	{
	int		str_len;
	int		i_str;
	int 	nzero;
	char	*nzero_str;
	char	triplette[4] = {'\0', '\0', '\0', '\0'};

	str_len = ft_strlen(str);
	i_str = 0;
	nzero = ((str_len - 1) / 3) * 3;
	if ((str_len % 3) == 1)
	{
		triplette[0] = str[0];
		check_3(&triplette, 1);
		i_str += 1;
	}
	else if ((str_len % 3) == 2)
	{
		triplette[0] = str[0];
		triplette[1] = str[1];
		check_3(&triplette, 1);
		i_str += 2;
	}
	while (i_str < (str_len - 1))
	{
		triplette[0] = str[i_str];
		triplette[1] = str[i_str + 1];
		triplette[2] = str[i_str + 2];
		check_3(&triplette, 3);
		i_str += 3;
		if (nzero >= 1)
		{
			nzero_str = one_and_nzero(nzero);
			// qui print dickt prende il valore della funzione che sta sopra
			// print_dict()
			free(nzero_str);
			nzero -= 3;
		}
	}
}
