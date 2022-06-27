class ReactiveState:
    def __init__(self, data):
        self._state = data
        self._total_changes = 0

    def get_state(self, key=None):
        if key is None:
            return self._state
        return self._get(key)

    def set_state(self, key=None, value=None):
        if key is None or value is None:
            return "A key and value must both be provided."
        self._set(key, value)
        return self._state

    def _get(self, key):
        self._track(self._state, key)
        return self._state[key]

    def _set(self, key, value):
        self._watch(self._state, key, value)
        if (self._state[key] != value):
            self._trigger(self._state, key, value)
        self._state[key] = value

    def _track(self, target, prop):
        print("track - Data get:", target, prop)

    def _watch(self, target, key, value):
        print("State is being changed: (old values)",
              target, "\n Key:", key, "\n new value:", value)

    def _trigger(self, target, key, value):
        self._total_changes += 1
        print("State has been changed, Total changes: {}".format(self._total_changes))


####
data = ReactiveState(
    {"name": "Derek", "age": 29, "occupation": "Software Engineer"})
print(data.get_state())
print(data.get_state("name"))

data.set_state("name", "Derek Bruckner")
data.set_state("occupation", "Software Developer")
