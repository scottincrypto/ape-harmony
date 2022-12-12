from typing import Optional

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (1666600000, 1666600000),
    "testnet": (1666700000, 1666700000),
    "devnet": (1666900000, 1666900000),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 1, **kwargs
) -> NetworkConfig:
    # Helper method to isolate `type: ignore` comments.
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )  # type: ignore


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class HarmonyConfig(PluginConfig):
    mainnet: NetworkConfig = _create_network_config()
    mainnet_fork: NetworkConfig = _create_local_config()
    testnet: NetworkConfig = _create_network_config()
    testnet_fork: NetworkConfig = _create_local_config()
    devnet: NetworkConfig = _create_network_config()
    devnet_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Harmony(Ethereum):
    @property
    def config(self) -> HarmonyConfig:  # type: ignore
        return self.config_manager.get_config("harmony")  # type: ignore
