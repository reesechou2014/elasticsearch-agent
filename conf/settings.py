#!/usr/bin/env python
# encoding: utf-8

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: settings.py
Created Time: 12/22/16 12:05
"""
import socket
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
pidfile = '/run/elasticsearch/es-agent.pid'
stdout = '/data/log/elasticsearch/es-agent.log'
stderr = '/data/log/elasticsearch/es-agent.err'
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
PORT = 9200

# URL = 'http://127.0.0.1:1988/v1/push'

OPEN_FALCON = BASE_DIR + '/open-falcon.yaml'
STATSD_FILE = BASE_DIR + '/statsd.yaml'

# keys for health page
traps1 = [
    "status",
    "active_primary_shards",
    "active_shards",
    "initializing_shards",
    "number_of_data_nodes",
    "number_of_nodes",
    "relocating_shards",
    "unassigned_shards"
]

# keys for cluster stats page
traps2 = [
    "thread_pool.index.active",
    # "thread_pool.index.completed",
    # "thread_pool.index.largest",
    "thread_pool.index.queue",
    "thread_pool.index.rejected",
    # "thread_pool.index.threads",
    # "thread_pool.search.completed"
    "thread_pool.search.rejected",
    "thread_pool.search.active",
    # "thread_pool.search.largest",
    "thread_pool.search.queue",
    # "thread_pool.search.threads",
    "thread_pool.bulk.active",
    "thread_pool.bulk.queue",
    "thread_pool.bulk.rejected",
    "http.current_open",
    "http.total_opened",
    "process.cpu.percent",
    "process.cpu.sys_in_millis",
    "process.cpu.total_in_millis",
    "process.cpu.user_in_millis",
    "process.mem.resident_in_bytes",
    "process.mem.share_in_bytes",
    "process.mem.total_virtual_in_bytes",
    "process.open_file_descriptors",
    "indices.docs.count",
    "indices.docs.deleted",
    "indices.flush.total",
    "indices.flush.total_time_in_millis",
    "indices.get.exists_time_in_millis",
    "indices.get.exists_total",
    "indices.get.missing_time_in_millis",
    "indices.get.missing_total",
    "indices.indexing.delete_time_in_millis",
    "indices.indexing.delete_total",
    "indices.indexing.index_time_in_millis",
    "indices.indexing.index_total",
    "indices.indexing.index_current",
    "indices.indexing.index_failed",
    "indices.merges.total_size_in_bytes",
    "indices.merges.total_time_in_millis",
    "indices.refresh.total",
    "indices.refresh.total_time_in_millis",
    "indices.search.fetch_time_in_millis",
    "indices.search.fetch_total",
    "indices.search.query_time_in_millis",
    "indices.search.query_total",
    "indices.store.throttle_time_in_millis",
    "indices.warmer.total",
    "indices.warmer.total_time_in_millis",
    "indices.segments.memory_in_bytes",
    "indices.segments.count",
    "jvm.mem.heap_committed_in_bytes",
    "jvm.mem.heap_max_in_bytes",
    "jvm.mem.heap_used_in_bytes",
    "jvm.mem.heap_used_percent",
    # "jvm.mem.non_heap_committed_in_bytes",
    # "jvm.mem.non_heap_used_in_bytes",
    "jvm.mem.pools.old.max_in_bytes",
    # "jvm.mem.pools.old.peak_max_in_bytes",
    # "jvm.mem.pools.old.peak_used_in_bytes",
    "jvm.mem.pools.old.used_in_bytes",
    "jvm.mem.pools.young.max_in_bytes",
    # "jvm.mem.pools.young.peak_max_in_bytes",
    # "jvm.mem.pools.young.peak_used_in_bytes",
    "jvm.mem.pools.young.used_in_bytes",
    "jvm.mem.pools.survivor.max_in_bytes",
    # "jvm.mem.pools.survivor.peak_max_in_bytes",
    # "jvm.mem.pools.survivor.peak_used_in_bytes",
    "jvm.mem.pools.survivor.used_in_bytes",
    "jvm.threads.count",
    "jvm.threads.peak_count",
    "jvm.gc.collectors.old.collection_count",
    "jvm.gc.collectors.old.collection_time_in_millis",
    "jvm.gc.collectors.young.collection_count",
    "jvm.gc.collectors.young.collection_time_in_millis",
    "jvm.buffer_pools.direct.count",
    "jvm.buffer_pools.direct.total_capacity_in_bytes",
    "jvm.buffer_pools.direct.used_in_bytes",
    "jvm.buffer_pools.mapped.count",
    "jvm.buffer_pools.mapped.total_capacity_in_bytes",
    "jvm.buffer_pools.mapped.used_in_bytes",
    "os.mem.used_in_bytes",
    "os.mem.total_in_bytes",
    "os.mem.free_in_bytes",
    "os.mem.free_percent",
    "os.mem.used_percent",
    "os.cpu_percent",
    "os.load_average",
    "transport.rx_size_in_bytes",
    "transport.rx_count",
    "transport.tx_size_in_bytes",
    "transport.tx_count"
]

GAUGE = [
    "active_primary_shards",
    "active_shards",
    "status",
    "number_of_data_nodes",
    "number_of_nodes",
    "unassigned_shards",
    "http.current_open",
    "initializing_shards",
    "jvm.buffer_pools.direct.count",
    "jvm.buffer_pools.direct.total_capacity_in_bytes",
    "jvm.buffer_pools.direct.used_in_bytes",
    "jvm.buffer_pools.mapped.count",
    "jvm.buffer_pools.mapped.total_capacity_in_bytes",
    "jvm.buffer_pools.mapped.used_in_bytes",
    "jvm.mem.heap_committed_in_bytes",
    "jvm.mem.heap_max_in_bytes",
    "jvm.mem.heap_used_in_bytes",
    "jvm.mem.heap_used_percent",
    # "jvm.mem.non_heap_committed_in_bytes",
    # "jvm.mem.non_heap_used_in_bytes",
    "jvm.mem.pools.old.max_in_bytes",
    # "jvm.mem.pools.old.peak_max_in_bytes",
    # "jvm.mem.pools.old.peak_used_in_bytes",
    "jvm.mem.pools.old.used_in_bytes",
    "jvm.mem.pools.survivor.max_in_bytes",
    # "jvm.mem.pools.survivor.peak_max_in_bytes",
    # "jvm.mem.pools.survivor.peak_used_in_bytes",
    "jvm.mem.pools.survivor.used_in_bytes",
    "jvm.mem.pools.young.max_in_bytes",
    # "jvm.mem.pools.young.peak_max_in_bytes",
    # "jvm.mem.pools.young.peak_used_in_bytes",
    "jvm.mem.pools.young.used_in_bytes",
    "jvm.threads.count",
    "jvm.threads.peak_count",
    "jvm_heap_p_of_RAM",
    "jvm_heap_p_used",
    "jvm.uptime_in_millis",
    "os.mem.used_in_bytes",
    "os.mem.total_in_bytes",
    "os.mem.free_in_bytes",
    "os.mem.free_percent",
    "os.mem.used_percent",
    "os.cpu_percent",
    "os.load_average",
    "process.cpu.percent",
    "process.cpu.sys_in_millis",
    "process.cpu.total_in_millis",
    "process.cpu.user_in_millis",
    "process.mem.resident_in_bytes",
    "process.mem.share_in_bytes",
    "process.mem.total_virtual_in_bytes",
    "process.open_file_descriptors",
    "indices.segments.count",
    "indices.segments.memory_in_bytes",
    "thread_pool.index.active",
    "thread_pool.bulk.active",
    "thread_pool.search.active",
    "thread_pool.index.queue",
    "thread_pool.bulk.queue",
    "thread_pool.search.queue",
    "relocating_shards"
]

COUNTER = [
    "http.total_opened",
    "indices.docs.count",
    "indices.docs.deleted",
    "indices.flush.total",
    "indices.flush.total_time_in_millis",
    "indices.get.exists_time_in_millis",
    "indices.get.exists_total",
    "indices.get.missing_time_in_millis",
    "indices.get.missing_total",
    "indices.indexing.delete_time_in_millis",
    "indices.indexing.delete_total",
    "indices.indexing.index_time_in_millis",
    "indices.indexing.index_total",
    "indices.indexing.index_current",
    "indices.indexing.index_failed",
    "indices.merges.total_size_in_bytes",
    "indices.merges.total_time_in_millis",
    "indices.refresh.total",
    "indices.refresh.total_time_in_millis",
    "indices.search.fetch_time_in_millis",
    "indices.search.fetch_total",
    "indices.search.query_time_in_millis",
    "indices.search.query_total",
    "indices.store.throttle_time_in_millis",
    "indices.warmer.total",
    "indices.warmer.total_time_in_millis",
    # "thread_pool.index.completed"
    "thread_pool.index.rejected",
    # "thread_pool.index.largest",
    # "thread_pool.index.threads",
    # "thread_pool.search.completed"
    "thread_pool.search.rejected",
    "thread_pool.bulk.rejected",
    # "thread_pool.search.largest",
    # "thread_pool.search.threads",
    "jvm.gc.collectors.old.collection_count",
    "jvm.gc.collectors.old.collection_time_in_millis",
    "jvm.gc.collectors.young.collection_time_in_millis",
    "jvm.gc.collectors.young.collection_count",
    "transport.rx_size_in_bytes",
    "transport.rx_count",
    "transport.tx_size_in_bytes",
    "transport.tx_count"
]

SEC_METRIC = {
    "indices.search.query_time_in_millis": "indices.search.query_total",
    "indices.search.fetch_time_in_millis": "indices.search.fetch_total",
    "indices.get.exists_time_in_millis": "indices.get.exists_total",
    "indices.get.missing_time_in_millis": "indices.get.missing_total",
    "indices.merges.total_size_in_bytes": "indices.merges.total_time_in_millis",
    "indices.flush.total": "indices.flush.total_time_in_millis",
    "indices.refresh.total": "indices.refresh.total_time_in_millis",
    "indices.indexing.index_time_in_millis": "indices.indexing.index_total",
    "indices.indexing.delete_time_in_millis": "indices.indexing.delete_total",
    "indices.warmer.total": "indices.warmer.total_time_in_millis",
    "jvm.gc.collectors.young.collection_time_in_millis": "jvm.gc.collectors.young.collection_count",
    "jvm.gc.collectors.old.collection_time_in_millis": "jvm.gc.collectors.old.collection_count",
}

if __name__ == '__main__':
    pass
