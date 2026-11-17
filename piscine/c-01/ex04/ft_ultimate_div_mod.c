/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 10:49:53 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/01/20 10:50:09 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	divres;
	int	modres;

	divres = *a / *b;
	modres = *a % *b;
	*a = divres;
	*b = modres;
}
