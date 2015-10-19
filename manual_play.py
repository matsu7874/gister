import player
import geister


def manual_play():
    players = [player.ManualPlayer(), player.Player()]
    g = geister.Geister(players)
    while not g.is_finish():
        status = g.get_status()
        if status['turn'] %2 == 0:
            cells = [['-' for j in range(6)] for i in range(6)]
            for y,x in status['active_goods']:
                cells[y][x]='g'
            for y,x in status['active_evils']:
                cells[y][x]='e'
            for y,x in status['opponent_goods']:
                cells[y][x]='X'
            for y,x in status['opponent_evils']:
                cells[y][x]='X'

            print('yx012345')
            for i in range(5,-1,-1):
                print(i,''.join(cells[i]))
            print('yx012345')
            print(status['captured'])
        g.play()
    status = g.get_status()
    print(status)
    print(status['winner'],status['reason'])

if __name__ == '__main__':
    manual_play()