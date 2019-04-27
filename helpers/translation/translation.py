from .en_us import EnUs


def register_module(injector):
    injector.singleton('translation', lambda _ : EnUs)