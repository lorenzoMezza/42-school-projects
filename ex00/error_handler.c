/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_handler.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 12:54:45 by mbrunial          #+#    #+#             */
/*   Updated: 2026/02/01 20:37:44 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	is_number_valid_edge_case(char *dummy)
{
	int	i;

	i = 0;
	if (dummy[i] == '\0')
		return (0);
	if (dummy[i] == '-' && dummy[i + 1] != '\0' && dummy[i + 1] == '0'
		&& dummy[i + 2] == '\0')
		return (1);
	return (2);
}

/*
 * is_number_valid returns 1 if the string contains only digits,
 * and 0 otherwise.
 *
 * 
 * It does NOT handle negative numbers, the '-' sign,
 * decimal points, or the special case "-0".
 */
char	*is_number_valid(char *str)
{
	int		i;
	int 	is_all_zero;
	int		start_with_zero;
	char	*dummy;

	i = 0;
	dummy = str;
	is_all_zero = 1;
	start_with_zero = 1;
	if (is_number_valid_edge_case(dummy) == 0)
		return (NULL);
	if (*dummy == '+')
		dummy += 1;
	if (is_number_valid_edge_case(dummy) == 1)
		return (dummy + 1);
	while (dummy[i])
	{
		if (!(dummy[i] >= '0' && dummy[i] <= '9'))
			return (NULL);
		else if (start_with_zero == 1 && dummy[i] == '0' && dummy[i + 1] != '\0'
			&& dummy[i + 1] != '0')
		{
			start_with_zero = 0;
			dummy = (dummy + i + 1);
			i = -1;
		}
		if (dummy[i] == '0')
		{
			is_all_zero = 0;
		}
		else
		{
			is_all_zero = 1;
		}
		i++;
	}
	if (!is_all_zero)
		return (dummy + i - 1);
	return (dummy);
}

/*
 * error_handler returns 1 if the arguments are valid,
 * and 0 if an error is detected.
 *
 * It checks that the number of arguments is correct
 * and that the first argument is a valid number.
 */
int	error_argn(int argn)
{
	if (argn > 3 || argn < 2)
	{
		write(1, "Error\n", 6);
		return (0);
	}
	return (1);
}
char	*error_arg(char **argv)
{
	char	*trimmed_str;
	
	if (!argv || !argv[1])  
	{
		write(1, "Error\n", 6);
		return (NULL);
	}
	
	trimmed_str = is_number_valid(argv[1]);
	if (trimmed_str == NULL)  
	{
		write(1, "Error\n", 6);
		return (NULL);
	}
	
	return (trimmed_str);
}
