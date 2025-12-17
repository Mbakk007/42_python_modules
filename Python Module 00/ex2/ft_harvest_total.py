# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-bakk <ael-bakk@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 12:38:33 by ael-bakk          #+#    #+#              #
#    Updated: 2025/12/14 12:49:58 by ael-bakk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    total = harvest1 + harvest2 + harvest3
    print(f"Total harvest: {total}")
