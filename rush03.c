/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush03.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lurossi <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 14:20:05 by lurossi           #+#    #+#             */
/*   Updated: 2026/01/17 15:53:26 by lurossi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char a);

void	righeInizioFine(int x)
{
	char posizione;

        posizione = 1;

	while(posizione <= x )
        {
                if(posizione == 1)
                        ft_putchar('A');
                else if(posizione == x)
                        ft_putchar('C');
		else
			ft_putchar('B');
                posizione++;
        }

}

void	righeCentro(int x)
{
	char posizione;

	posizione = 1;
	while(posizione <= x )
	{
		if(posizione == 1 || posizione == x)
			ft_putchar('B');
		else
			ft_putchar(' ');
		posizione++;
	}
}

void    rush(int x, int y)
{
	if(x <= 0 || y <= 0)
	{
		return;
	}
	
		char loopCentrale;
		loopCentrale = y;
        	righeInizioFine(x);
        	ft_putchar('\n');
		loopCentrale--;
        while(loopCentrale > 1)
        {
                righeCentro(x);
		ft_putchar('\n');
                loopCentrale--;
        }
	if( y > 1){
        	righeInizioFine(x);
	}
}
