/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 11:08:30 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/01/17 11:31:13 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	index;
	int				is_null;

	index = 0;
	is_null = 0;
	while (n--)
	{
		if (!*(src + index))
		{
			is_null = 1;
		}
		if (is_null)
		{
			*(dest + index) = '\0';
		}
		else
		{
			*(dest + index) = *(src + index);
		}
		index++;
	}
	return (dest);
}
