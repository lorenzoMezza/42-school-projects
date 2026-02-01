/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ginevra.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/01 22:17:34 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/02/01 22:17:37 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "rush02.h"

void	check_2(char *str, t_dict *dict, int dictSize);
void	check_1(char *str, t_dict *dict, int dictSize);

void	check_3(char *str, t_dict *dict, int dictSize)
{
	if (str[0] == '0' && str[1] == '0' && str[2] == '0')
	{
		return ;
	}
	else if (str[0] == '0' && str[1] == '0' && str[2] != '0')
	{
		check_1(str + 2, dict, dictSize);
	}
	else if (str[0] == '0' && str[1] != '0')
	{
		check_2(str + 1, dict, dictSize);
	}
	else
	{
		continua_check_3(str, dict, dictSize);
	}
}

void	continua_check_3(char *str, t_dict *dict, int dictSize)
{
	char	temp[4];
	char	*value;

	temp[0] = str[0];
	temp[1] = '0';
	temp[2] = '0';
	temp[3] = '\0';
	
	value = ft_get_value(dict, dictSize, temp);
	if (value)
	{
		ft_putstr(value);
		ft_putstr(" ");
	}
	check_2(str + 1, dict, dictSize);
}

void	check_2(char *str, t_dict *dict, int dictSize)
{
	char	temp[3];
	char	*value;

	if (str[0] == '0' && str[1] == '0')
	{
		return ;
	}
	else if (str[0] == '0' && str[1] != '0')
	{
		check_1(str + 1, dict, dictSize);
		return ;
	}
	else if (str[1] == '0')
	{
		temp[0] = str[0];
		temp[1] = str[1];
		temp[2] = '\0';
		value = ft_get_value(dict, dictSize, temp);
		if (value)
			ft_putstr(value);
	}
	else if (str[0] == '1')
	{
		finalize_check2(str, dict, dictSize);
	}
	else
	{
		temp[0] = str[0];
		temp[1] = '0';
		temp[2] = '\0';
		value = ft_get_value(dict, dictSize, temp);
		if (value)
		{
			ft_putstr(value);
			ft_putstr(" ");
		}
		check_1(str + 1, dict, dictSize);
	}
}

void	finalize_check2(char *str, t_dict *dict, int dictSize)
{
	char	temp[3];
	char	*value;

	temp[0] = str[0];
	temp[1] = str[1];
	temp[2] = '\0';
	
	value = ft_get_value(dict, dictSize, temp);
	if (value)
		ft_putstr(value);
}

void	check_1(char *str, t_dict *dict, int dictSize)
{
	char	temp[2];
	char	*value;

	if (str[0] == '0')
		return ;

	temp[0] = str[0];
	temp[1] = '\0';

	value = ft_get_value(dict, dictSize, temp);
	if (value)
		ft_putstr(value);
}