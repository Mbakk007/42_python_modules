# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-bakk <ael-bakk@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 12:57:41 by ael-bakk          #+#    #+#              #
#    Updated: 2025/12/14 13:04:38 by ael-bakk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    if days <= 0:
        print("Harvest time!")
        return
    while i <= days:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
