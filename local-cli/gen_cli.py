from omegaconf import DictConfig, OmegaConf
from hydra.core.hydra_config import HydraConfig
import hydra

@hydra.main(config_path="../config", config_name="defaults")
def gen_cli(cfg: DictConfig) -> None:
    cfg = OmegaConf.to_container(cfg, resolve=True) # resolve all interpolations eagerly
    print(OmegaConf.to_yaml(cfg))
    print(HydraConfig.get().overrides.task)

if __name__ == "__main__":
    gen_cli()