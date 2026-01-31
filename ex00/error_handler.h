/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_handler.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 12:54:45 by mbrunial          #+#    #+#             */
/*   Updated: 2026/01/31 19:07:44 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <unistd.h>

char	*is_number_valid_edge_case(char *dummy)
{
	int	i;

	i = 0;
	if (dummy[i] == '\0')
		return (NULL);
	if (dummy[i] == '-' && dummy[i + 1] != '\0' && dummy[i + 1] == '0'
		&& dummy[i + 2] == '\0')
		return (dummy + 1);
	return (NULL);
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
	int		start_with_zero;
	char	*dummy;

	i = 0;
	start_with_zero = 1;
	dummy = str;
	if (is_number_valid_edge_case == NULL)
		return (NULL);
	else
		return (is_number_valid_edge_case);
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
		i++;
	}
	return (dummy);
}

/*
 * error_handler returns 1 if the arguments are valid,
 * and 0 if an error is detected.
 *
 * It checks that the number of arguments is correct
 * and that the first argument is a valid number.
 */
char	*error_arg(int argn, char **argv)
{
	char	*trimmed_str;

	if (argn > 3 || argn < 2)
	{
		write(1, "Error\n", 6);
		return (NULL);
	}
	trimmed_str = is_number_valid(argv[1]);
	if (trimmed_str == 0)
	{
		write(1, "Error\n", 6);
		return (NULL);
	}
	return (trimmed_str);
}
