import setuptools
from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            return "cp38", "abi3", plat

        return python, abi, plat


setuptools.setup(
    cffi_modules=[
        "src/_cffi_src/build_opus.py:ffibuilder",
        "src/_cffi_src/build_vpx.py:ffibuilder",
    ],
    cmdclass={"bdist_wheel": bdist_wheel_abi3},
    install_requires=[
        "aioice @ git+ssh://git@github.com/mduppes/aioice#limit_udp_port",
        "av>=9.0.0,<13.0.0",
        "cffi>=1.0.0",
        "cryptography>=42.0.0",
        'dataclasses; python_version < "3.7"',
        "google-crc32c>=1.1",
        "pyee>=9.0.0",
        "pylibsrtp>=0.10.0",
        "pyopenssl>=24.0.0",
    ]
)
