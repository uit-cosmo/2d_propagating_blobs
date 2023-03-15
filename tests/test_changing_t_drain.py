from blobmodel import Model, DefaultBlobFactory, BlobShapeImpl
import xarray as xr
import numpy as np


# use DefaultBlobFactory to define distribution functions fo random variables
bf = DefaultBlobFactory(A_dist="deg", wx_dist="deg", vx_dist="deg", vy_dist="zeros")

t_drain = np.linspace(2, 1, 10)

tmp = Model(
    Nx=10,
    Ny=1,
    Lx=10,
    Ly=0,
    dt=1,
    T=1000,
    blob_shape=BlobShapeImpl("exp"),
    t_drain=t_drain,
    periodic_y=False,
    num_blobs=10000,
    blob_factory=bf,
)


tmp.make_realization(file_name="test_t_drain.nc", speed_up=True, error=1e-2)


def test_decreasing_t_drain():

    ds = xr.open_dataset("test_t_drain.nc")
    model_profile = ds.n.isel(y=0).mean(dim=("t"))

    x = np.linspace(0, 10, 10)
    t_p = 1
    t_w = 1 / 10
    amp = 1
    v_p = 1.0
    t_loss = 2.0
    t_d = t_loss * t_p / (t_loss + t_p)

    analytical_profile = (
        1 / np.sqrt(np.pi) * t_d / t_w * amp * np.exp(-x / (v_p * t_loss))
    )
    assert (model_profile.values[2:] < analytical_profile[2:]).all()


test_decreasing_t_drain()
