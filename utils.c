/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/01 22:44:13 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/02/01 22:44:16 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "rush02.h"
#include <unistd.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

void	ft_putstr(char *str)
{
	write(1, str, ft_strlen(str));
}

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
#include <stdlib.h>  // per malloc
#include <string.h>  // per strlen

char *ft_substr(char *s, unsigned int start, size_t len) {
    char *substr;
    size_t i;

    // Se la stringa di partenza è NULL o la lunghezza della sottostringa è 0
    if (!s) return NULL;

    // Se 'start' è più grande della lunghezza di 's', restituiamo una stringa vuota
    if (start >= strlen(s)) {
        substr = (char *)malloc(1);  // Solo per il terminatore NULL
        if (!substr) return NULL;
        substr[0] = '\0';
        return substr;
    }

    // Altrimenti, calcoliamo la lunghezza della sottostringa
    // Se la lunghezza di 's' da 'start' è più corta di 'len', prendiamo la lunghezza rimanente
    size_t substr_len = strlen(s + start) < len ? strlen(s + start) : len;

    // Allochiamo memoria per la sottostringa + 1 per il terminatore NULL
    substr = (char *)malloc(substr_len + 1);
    if (!substr) return NULL;  // Se malloc fallisce

    // Copiamo la sottostringa
    for (i = 0; i < substr_len; i++) {
        substr[i] = s[start + i];
    }

    // Aggiungiamo il terminatore NULL alla fine
    substr[substr_len] = '\0';

    return substr;
}
