'''This module implements concrete reset rule for crash'''

from markov.reset.abstract_reset_rule import AbstractResetRule
from markov.reset.constants import AgentCtrlStatus, AgentInfo
from markov.track_geom.track_data import TrackData
from markov.metrics.constants import EpisodeStatus

class CrashResetRule(AbstractResetRule):
    name = EpisodeStatus.CRASHED.value

    def __init__(self, agent_name):
        super(CrashResetRule, self).__init__(CrashResetRule.name)
        self._track_data = TrackData.get_instance()
        self._agent_name = agent_name

    def _update(self, agent_status):
        '''Update the crash reset rule done flag

        Args:
            agent_status (dict): agent status dictionary

        Returns:
            dict: dictionary contains the agent crash info
        '''
        crashed_object_name = self._track_data.get_collided_object_name(
            self._agent_name)
        self._done = crashed_object_name != ''
        return {AgentInfo.CRASHED_OBJECT_NAME.value: crashed_object_name,
                AgentInfo.START_NDIST.value: agent_status[AgentCtrlStatus.START_NDIST.value]}
