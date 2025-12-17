# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-bakk <ael-bakk@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 13:05:16 by ael-bakk          #+#    #+#              #
#    Updated: 2025/12/14 13:19:04 by ael-bakk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(i):
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        recursive(i + 1)
    recursive(1)
