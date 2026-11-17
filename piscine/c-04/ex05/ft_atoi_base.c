/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 14:28:15 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/01/26 14:28:21 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
int	get_base_len(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-' || base[i] <= 32)
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	if (i <= 1)
		return (0);
	return (i);
}

int	char_to_val(char c, char *base)
{
	int	i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

int	skip_spaces_and_sign(char **str)
{
	int	sign;

	sign = 1;
	while (**str && (**str == ' ' || (**str >= 9 && **str <= 13)))
		(*str)++;
	while (**str == '+' || **str == '-')
	{
		if (**str == '-')
			sign *= -1;
		(*str)++;
	}
	return (sign);
}

int	ft_atoi_base(char *str, char *base)
{
	int	base_len;
	int	sign;
	int	result;
	int	val;

	base_len = get_base_len(base);
	if (!base_len)
		return (0);
	sign = skip_spaces_and_sign(&str);
	result = 0;
	while (*str)
	{
		val = char_to_val(*str, base);
		if (val == -1)
			break ;
		result = result * base_len + val;
		str++;
	}
	return (result * sign);
}
