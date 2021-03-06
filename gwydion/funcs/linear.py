from gwydion.base import Base
from gwydion.exceptions import GwydionError


class Linear(Base):
    """
    Linear function (i.e. straight line). Returned function is

        y = m * x + c

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    m : Float, integer, or None (default).
        Gradient of straight line function. If None, defaults to a randomised "typical" value.
    c : Float, integer, or None (default).
        y-intercept of straight line function. If None, defaults to a randomised "typical" value.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (0, 10).
    rand : Float or integer.
        TThe amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.5.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Linear()  # Default params, returns a "normal" straight line.
    >>>> Linear(N=1000)  # Increase the number of data points.
    >>>> Linear(m=0, c=0)  # Horizontal line with randomness
    >>>> Linear(rand=None)  # Turn off randomness.
    >>>> Linear(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, m=None, c=None, xlim=(0, 10), rand=0.5, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)

        self.set_variables(m, c)

    def set_variables(self, m, c):

        for var in [m, c]:
            if var is not None and not isinstance(var, (float, int)):
                raise GwydionError('Variables must be either float, int, or None.')

        if m is None:
            self.m = (self.random.rand() + 0.5) * 2
        else:
            self.m = m

        if c is None:
            self.c = (self.random.rand() - 0.5) * 10
        else:
            self.c = c

    def func(self, x):
        m = self.m
        c = self.c

        return m * x + c
