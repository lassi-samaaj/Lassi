import os

from ਲੱਸੀ.ਵਿਆ.ਭਾ import ਵਿਆਕਰਣ_ਵਾਧਾ


def ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ(ਪਾਠ):
    for ਅ in ਪਾਠ:
        yield '{} '.format(ਅ) if len(ਅ.strip()) and not ਅ.strip(' \t').endswith('\n') else ਅ


class ਲਾਰਕ_ਵਿਆਕਰਣ(ਵਿਆਕਰਣ_ਵਾਧਾ):
    ਵਿਆ = os.path.join(os.path.split(__file__)[0], 'ਲਾਰਕ.lark')
    ਵਾਧਾ = '.lark'
    ਸਰੋਤ_ਭਾ = 'en'

    def __init__(ਖੁਦ):
        super().__init__()
        ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = dict(postproc=ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ)


if __name__ == '__main__':
    g = ਲਾਰਕ_ਵਿਆਕਰਣ()
    g.ਦਸਤ_ਸਰੋਤ_ਅਨੁ_ਬੲਾਉ()
