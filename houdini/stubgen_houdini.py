from __future__ import absolute_import, annotations, division, print_function

import re

import mypy.stubgen
import mypy.stubgenc
from mypy.fastparse import parse_type_comment
from mypy.stubgen import main
from mypy.stubgenc import ArgSig
from mypy.stubgenc import DocstringSignatureGenerator as CDocstringSignatureGenerator
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    def is_defined_in_module(self, obj: object) -> bool:
        if self.module_name == 'mari' and getattr(obj, '__module__', '').startswith(
            'mari.Mari'
        ):
            return True
        return super().is_defined_in_module(obj)

    # def get_sig_generators(self) -> list[SignatureGenerator]:
    #     return [DocstringSignatureGenerator()]


mypy.stubgen.CStubGenerator = CStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.CStubGenerator = CStubGenerator  # type: ignore[misc]
