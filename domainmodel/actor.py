class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__coworkers: set = set()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if (colleague not in self.__coworkers):
            self.__coworkers.add(colleague)
    
    def check_if_this_actor_worked_with(self, colleague):
        if (colleague not in self.__coworkers):
            return False
        return True

class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Harry Potter")
        assert repr(actor1) == "<Actor Harry Potter>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None
        actor4 = Actor("Ronald Weasley")
        assert repr(actor4) == "<Actor Ronald Weasley>"
        #assert actor1 == actor4
        assert actor1 == actor1
        assert actor1 < actor4
        #assert actor4 < actor1
        #assert hash(actor1) == hash(actor4)
        assert hash(actor4) == hash(actor4)
        thing1 = actor1.check_if_this_actor_worked_with(actor4)
        assert thing1 == 0
        thing = actor1.add_actor_colleague(actor4)
        thing1 = actor1.check_if_this_actor_worked_with(actor4)
        assert thing1 == 1
