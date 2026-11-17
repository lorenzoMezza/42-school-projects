/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 17:55:32 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/01/29 17:55:35 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

static int	total_len(int size, char **strs, char *sep)
{
	int	i;
	int	len;

	i = 0;
	len = 0;
	while (i < size)
	{
		len += ft_strlen(strs[i]);
		if (i < size - 1)
			len += ft_strlen(sep);
		i++;
	}
	return (len);
}

static void	fill_str(char *res, int size, char **strs, char *sep)
{
	int	i;
	int	j;
	int	k;

	i = 0;
	k = 0;
	while (i < size)
	{
		j = 0;
		while (strs[i][j])
			res[k++] = strs[i][j++];
		j = 0;
		while (sep[j] && i < size - 1)
			res[k++] = sep[j++];
		i++;
	}
	res[k] = '\0';
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*res;

	if (size == 0)
	{
		res = malloc(1);
		if (!res)
			return (NULL);
		res[0] = '\0';
		return (res);
	}
	res = malloc(total_len(size, strs, sep) + 1);
	if (!res)
		return (NULL);
	fill_str(res, size, strs, sep);
	return (res);
}
