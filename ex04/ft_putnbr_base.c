/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 15:12:05 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/01/26 15:12:08 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	is_valid_base(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-')
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	if (i > 1)
		return (i);
	return (0);
}

int	convert_to_base(long nbr, char *base, char *buffer)
{
	int	base_len;
	int	index;

	index = 0;
	base_len = is_valid_base(base);
	if (!base_len)
		return (0);
	if (nbr == 0)
	{
		buffer[index] = base[0];
		index++;
		return (index);
	}
	while (nbr > 0)
	{
		buffer[index] = base[nbr % base_len];
		nbr /= base_len;
		index++;
	}
	return (index);
}

void	ft_putnbr_base(int nbr, char *base)
{
	long	lnbr;
	char	buffer[32];
	int		index;

	lnbr = nbr;
	if (lnbr < 0)
	{
		write(1, "-", 1);
		lnbr = -lnbr;
	}
	index = convert_to_base(lnbr, base, buffer);
	while (index > 0)
	{
		index--;
		write(1, &buffer[index], 1);
	}
}
