# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-bakk <ael-bakk@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 12:54:32 by ael-bakk          #+#    #+#              #
#    Updated: 2025/12/14 12:56:26 by ael-bakk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
