/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush03.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lurossi <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 14:20:05 by lurossi           #+#    #+#             */
/*   Updated: 2026/01/18 14:33:54 by lurossi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
void	ft_putchar(char a);

void	righe_inizio_fine(int x, int volta)
{
	int	posizione;

	posizione = 1;
	while (posizione <= x)
	{
		if (posizione == 1)
		{
			if (volta == 1)
				ft_putchar('A');
			else
				ft_putchar('C');
		}
		else if (posizione == x)
		{
			if (volta == 1)
				ft_putchar('A');
			else
				ft_putchar('C');
		}
		else
			ft_putchar('B');
		posizione++;
	}
}

void	righe_centro(int x)
{
	int	posizione;

	posizione = 1;
	while (posizione <= x)
	{
		if (posizione == 1 || posizione == x)
			ft_putchar('B');
		else
			ft_putchar(' ');
		posizione++;
	}
}

void	rush(int x, int y)
{
	int	loop_centrale;

	loop_centrale = y;
	if (x <= 0 || y <= 0)
	{
		return ;
	}
	righe_inizio_fine(x, 1);
	ft_putchar('\n');
	loop_centrale--;
	while (loop_centrale > 1)
	{
		righe_centro(x);
		ft_putchar('\n');
		loop_centrale--;
	}
	if (y > 1)
	{
		righe_inizio_fine(x, 2);
		ft_putchar('\n');
	}
}
