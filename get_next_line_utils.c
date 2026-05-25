/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <lmezzaba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:54:17 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/25 12:55:20 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	has_newline(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (0);
	while (s[i])
	{
		if (s[i] == '\n')
			return (1);
		i++;
	}
	return (0);
}

char	*substr_dup(char *s, int start, int len)
{
	char	*out;
	int		i;

	i = 0;
	if (!s || len <= 0)
		return (NULL);
	out = malloc(len + 1);
	if (!out)
		return (NULL);
	while (i < len && s[start + i])
	{
		out[i] = s[start + i];
		i++;
	}
	out[i] = '\0';
	return (out);
}
