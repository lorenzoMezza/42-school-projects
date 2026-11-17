/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <lmezzaba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 12:54:19 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/25 12:55:24 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (0);
	while (s[i])
		i++;
	return (i);
}

static char	*join_and_free(char *s1, char *s2, int n)
{
	char	*res;
	int		i;
	int		j;
	int		len1;

	len1 = ft_strlen(s1);
	res = malloc(len1 + n + 1);
	if (!res)
		return (NULL);
	i = 0;
	while (i < len1)
	{
		res[i] = s1[i];
		i++;
	}
	j = 0;
	while (j < n)
	{
		res[i + j] = s2[j];
		j++;
	}
	res[i + j] = '\0';
	free(s1);
	return (res);
}

static int	fill_buffer(int fd, char **stash, char *buf)
{
	int	r;

	r = 1;
	while (!has_newline(*stash) && r > 0)
	{
		r = read(fd, buf, BUFFER_SIZE);
		if (r <= 0)
			return (r);
		buf[r] = '\0';
		*stash = join_and_free(*stash, buf, r);
		if (!*stash)
			return (-1);
	}
	return (1);
}

static char	*cut_line(char **stash)
{
	char	*line;
	char	*rest;
	int		i;

	i = 0;
	if (!*stash || !**stash)
		return (NULL);
	while ((*stash)[i] && (*stash)[i] != '\n')
		i++;
	if ((*stash)[i] == '\n')
		i++;
	line = substr_dup(*stash, 0, i);
	rest = substr_dup(*stash, i, ft_strlen(*stash) - i);
	free(*stash);
	*stash = rest;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*buf;
	char		*line;
	int			status;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
		return (NULL);
	status = fill_buffer(fd, &stash, buf);
	free(buf);
	if (status == 0)
	{
		line = stash;
		stash = NULL;
		return (line);
	}
	if (status < 0)
		return (NULL);
	return (cut_line(&stash));
}
