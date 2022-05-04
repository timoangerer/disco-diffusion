from omegaconf import DictConfig, OmegaConf
from hydra.core.hydra_config import HydraConfig
import hydra
import re
import api as API

@hydra.main(config_path="../config", config_name="defaults")
def gen_cli(cfg: DictConfig) -> None:
    overrides = list(HydraConfig.get().overrides.task)
    overrides = list(filter(lambda it: not bool(re.search(r"(sweep)", it)), overrides)) # remove sweep variables
    overrides_cfg = OmegaConf.from_cli(overrides)
    overrides_cfg["batch_name"] = cfg["batch_name"]
    print(OmegaConf.to_yaml(overrides_cfg))

    API.create_job(OmegaConf.to_container(overrides_cfg))


if __name__ == "__main__":
    gen_cli()