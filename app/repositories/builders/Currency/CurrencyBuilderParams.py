from dataclasses import dataclass

from repositories.builders.BuilderParams import BuilderParams


@dataclass
class CurrencyBuilderParams(BuilderParams):

    only_active: bool
