/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ccrucian <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/18 16:23:34 by ccrucian          #+#    #+#             */
/*   Updated: 2026/01/18 16:35:29 by ccrucian         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

void	inizio(int x)
{
	char	i;

	i = 1;
	while (i <= x)
	{
		if (i == 1)
			ft_putchar('o');
		else if (i == x)
			ft_putchar('o');
		else
			ft_putchar('-');
		i++;
	}
}

void	fine(int x)
{
	char	f;

	f = 1;
	while (f <= x)
	{
		if (f == 1)
			ft_putchar('o');
		else if (f == x)
			ft_putchar('o');
		else
			ft_putchar('-');
		f++;
	}
}

void	lati(int x)
{
	char	j;

	j = 1;
	while (j <= x)
	{
		if (j == 1 || j == x)
			ft_putchar('|');
		else
			ft_putchar(' ');
		j++;
	}
}

void	rush(int x, int y)
{
	char	loop;

	loop = y;
	if (x <= 0 || y <= 0)
		return ;
	inizio(x);
	ft_putchar('\n');
	loop--;
	while (loop > 1)
	{
		lati(x);
		ft_putchar('\n');
		loop--;
	}
	if (y > 1)
	{
		fine(x);
		ft_putchar('\n');
	}
}
