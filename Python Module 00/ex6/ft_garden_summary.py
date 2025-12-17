# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-bakk <ael-bakk@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 13:19:31 by ael-bakk          #+#    #+#              #
#    Updated: 2025/12/14 13:22:44 by ael-bakk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    Plants = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {Plants}")
    print("Status: Growing well!")
