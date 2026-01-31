/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbrunial <mbrunial@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 11:26:01 by mbrunial          #+#    #+#             */
/*   Updated: 2026/01/31 18:49:26 by mbrunial         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
Here Write main that call all the function, possibly write all the  fcuntion
outside the main.c file so it will  be divied in files with logical
functionality.
*/
#include <unistd.h>
#include <stdio.h>
#include "error_handler.h"

// here write the call to function
char	*is_number_valid(char *str);

char	*error_arg(int argn, char **argv);

int	main(int argn, char **argv)
{
	printf("%s", error_arg(argn, argv));


	return (0);
}
