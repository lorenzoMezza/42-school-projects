/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 11:26:01 by mbrunial          #+#    #+#             */
/*   Updated: 2026/02/01 20:40:12 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include "rush02.h"


int	main(int argn, char **argv)
{
	char *number;
	error_argn(argn);

	number = error_arg(argv);
	int sized = 0;
	int *size = &sized;
	t_dict	* dict;
	
	dict = 	ft_parse_dict(argv[2],  size);
	argn++;
	
	str_start(number,dict, *size);
	

	

	return (0);
}
