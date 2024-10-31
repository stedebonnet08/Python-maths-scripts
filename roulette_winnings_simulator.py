#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random           # for RNG
import time   # to seed RNG with UNIX time


# "Monte-Carlo"-esque simulation of playing
# (european) Roulette Red/Black with a strategy of
# doubling the bet each time you lose.
# Do many, MANY rounds and calculate win/loss

# Spoiler: You win your basic bet, each time
# but you better haver a deep, deep pocket 'cause you absolutely
# have to double up along each and any losing streak!

# constants:
NR_SIMULATIONS = 10000  # Number of "rounds" where a round is to play
                        # and keep doubling up along lose streaks until winning
WIN_NUMBERS = (32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3)  # Red Numbers
TABLE_NUMBERS = 37      # 37 Pockets on european Roulette table
WIN_PAYOUT_FACTOR=2     # x2 for Red/Black
INITIAL_BET=1

# simulate playing a single roulette bet on Red
# win_nrs = red numbers; table_nrs = total numbers on the Roulette wheel
def play_red_black(win_nrs, table_nrs):
    # seed RNG with UNIX epoch time
    random.seed(time.time())
    # get a winner out of 0 to 36
    winning_nr = random.randint(0, table_nrs - 1)
    # ... and output and return accordingly
    if (winning_nr in win_nrs):
        #print(f"WIN! {winning_nr} is a red number!")
        return True
    else:
        #print(f"LOSS! {winning_nr} isn't a red number!")
        return False

# simmulate one round of doubling up through losses until winning
# bet_amount = starting bet; win_payout_factor = factor to raise bet(x2 in R/B)
def play_until_win(bet_amount, win_payout_factor):

    current_bet = bet_amount
    cumulated_losses = 0

    # initial 1st game in order to get a BOOL for win/loss
    win_loss = play_red_black(WIN_NUMBERS, TABLE_NUMBERS)
    no_until_win = 1

    # as long as I lose...
    while (not win_loss):
        # tally up losses, count along and calculate next bet
        cumulated_losses = cumulated_losses + current_bet
        no_until_win += 1
        current_bet = current_bet * win_payout_factor
        # then play next round
        win_loss = play_red_black(WIN_NUMBERS, TABLE_NUMBERS)

    # after 1st win, get winnings and net p.o.
    winnings = current_bet
    net_payout = winnings - cumulated_losses
    # return these
    return no_until_win, winnings, cumulated_losses, net_payout

# now simulate many such rounds
def simulate_games(sim_no = NR_SIMULATIONS):

    # total_played = total spins of the wheel; max_bet_uses = how deep your
    # pockets gotta get (highest bet ever)
    total_played = 0
    max_bet_used = 0
    cumulated_payout = 0

    # go through those rounds
    for i in range(sim_no + 1):
        # play a round, print some info about that round
        played_games, win_money, cumulated_losses, net_po = \
            play_until_win(INITIAL_BET, WIN_PAYOUT_FACTOR)

        print(f'{played_games}: Bet: {win_money} EUR;', end=' ')
        print(f'{cumulated_losses} EUR lost. Net: {net_po} EUR', end='\n\n')

        if (win_money > max_bet_used):
            # new highest bet overall
            max_bet_used = win_money

        # tally up totals
        total_played += played_games
        cumulated_payout += net_po

    # and return them
    return total_played, max_bet_used, cumulated_payout


def main():
    # counting one further in order to equalize output
    nr_sims = NR_SIMULATIONS + 1
    # run total x rounds simulation, give a summary output
    tot_plyd, max_bet, cum_po = simulate_games()
    print(f'SUMMARY: {tot_plyd} games played over {nr_sims} rounds', end='\n')
    print(f'Maximum necessary bet: {max_bet}; cumulated payout: {cum_po}')

    return 0

# check for main (for library functionality)
if __name__ == '__main__':
    main()

