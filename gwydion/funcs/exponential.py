from gwydion.base import np, Base
from gwydion.exceptions import GwydionError


class Exponential(Base):
    """
    Exponential function (power law). Returned function is

        y = I * base**(k*x)

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    base : Float, integer, or None
        Base for function. If None, defaults to e = 2.718....
    I : Float, integer, or None.
        Intensity of function. If None, defaults to a random value around 1.0.
    k : Float, integer, or None.
        Amplitude of the exponent. If None, defaults to a random value around 0.0
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Float, integer, or None.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.1.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Exponential()  # Default params, returns a "normal" exponential.
    >>>> Exponential(N=1000)  # Increase the number of data points.
    >>>> Exponential(k=-1)  # Exponential decay.
    >>>> Exponential(add_rand=None)  # Turn off randomness.
    >>>> Exponential(seed=1234)  # Seeded RNG

    """

    def __init__(self, N=100, base=None, I=None, k=None, xlim=(-10, 10), rand=0.1, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)

        self.set_variables(base, I, k)

    def set_variables(self, base, I, k):

        for var in [I, k]:
            if var is not None and not isinstance(var, (float, int)):
                raise GwydionError('Variables must be either float, int, or None.')

        defaults = {'base': np.e,
                    'I': 1.0 + (self.random.rand() - 0.5) * 0.5,
                    'k': (self.random.rand() - 0.5) * 0.5}

        for key, val in list(defaults.items()):
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

    def func(self, x):
        I, k, base = self.I, self.k, self.base

        return I * np.power(base, self.k * x)
