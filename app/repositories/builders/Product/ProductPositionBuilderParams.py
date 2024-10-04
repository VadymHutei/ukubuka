from dataclasses import dataclass

from repositories.builders.BuilderParams import BuilderParams


@dataclass
class ProductPositionBuilderParams(BuilderParams):

    only_active: bool = False
