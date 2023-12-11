import project


def test_santa_says(capsys):
    project.santa_says("hello")
    captured = capsys.readouterr()
    assert captured.out=="🎅:hello\n"

def test_check_player():
    name="vic"
    players=["clau","isa"]
    assert project.check_player(name,players)==True
    players.append(name)
    assert project.check_player(name,players)==False
    name="1"
    assert project.check_player(name,players)==False


def test_check_gifted():
    player="a"
    gifted="b"
    assignated=[]
    assert project.check_gifted(player,gifted,assignated)==True
    assignated.append(gifted)
    assert project.check_gifted(player,gifted,assignated)==False
    assignated=[]
    player=gifted
    assert project.check_gifted(player,gifted,assignated)==False

def test_check_giveaway():
    players=["a","b"]
    assignated=["a"]
    assert project.check_giveaway(players,assignated)==False
    assignated.append("b")
    assert project.check_giveaway(players,assignated)==False
    assignated=["b","a"]
    assert project.check_giveaway(players,assignated)==True
    assignated=["b","a","b"]
    players=["a","b","b"]
    assert project.check_giveaway(players,assignated)==False


