
import json
from normalizer.modules.basenormalizer import BaseNormalizer

import sys


class RdphoneyEvents(BaseNormalizer):
    channels = ('rdphoney.sessions',)

    def normalize(self, data, channel, submission_timestamp, ignore_rfc1918=True):
        o_data = self.parse_record_data(data)
        sys.stdout.write("o_data: %s" % o_data + "\n")

        if ignore_rfc1918 and self.is_RFC1918_addr(o_data['peerIP']):
            return []

        session = {
            'timestamp': submission_timestamp,
            'source_ip': o_data['peerIP'],
            'source_port': o_data['peerPort'],
            'destination_port': o_data['hostPort'],
            'honeypot': 'rdphoney',
            'protocol': 'rdp',
        }

        relations = [{'session': session}, ]

        return relations
