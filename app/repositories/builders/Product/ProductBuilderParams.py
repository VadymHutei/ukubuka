from dataclasses import dataclass

from repositories.builders.BuilderParams import BuilderParams


@dataclass
class ProductBuilderParams(BuilderParams):

    only_active: bool = False
