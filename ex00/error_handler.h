/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_handler.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 12:54:45 by mbrunial          #+#    #+#             */
/*   Updated: 2026/01/31 12:54:55 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <unistd.h>

/*
 * is_number_valid returns 1 if the string contains only digits,
 * and 0 otherwise.
 *
 * It does NOT handle negative numbers, the '-' sign,
 * decimal points, or the special case "-0".
 */
int	is_number_valid(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (!(str[i] >= '0' && str[i] <= '9'))
		{
			return (0);
		}
		i++;
	}
	return (1);
}

/*
 * error_handler returns 1 if the arguments are valid,
 * and 0 if an error is detected.
 *
 * It checks that the number of arguments is correct
 * and that the first argument is a valid number.
 */
int	error_handler(int argn, char **argv)
{
	if (argn > 3 || argn < 2)
	{
		write(1, "Error\n", 6);
		return (0);
	}
	else if (is_number_valid(argv[1]) == 0)
	{
		write(1, "Error\n", 6);
		return (0);
	}
	return (1);
}
