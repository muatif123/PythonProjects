# Importing the required libraries
from os import stat
from tracemalloc import Snapshot
import boto3
import datetime

# Defining a class for RDS
class RDS(object):

    def __init__(self, region):
        super().__init__()
        self.rds = boto3.client('rds', region)

    def cleanup_snapshot(self):
        self._cleanup_snapshot_instance()
        self._cleanup_snapshots_clusters()

    def cleanup_instances(self):
        clusters = self.rds.describe_db_clusters()
        for cluster in clusters['DBClusters']:
            self._cleanup_cluster(cluster)
        instances = self.rds.describe_db_instances()
        for instance in instances['DBInstances']:
            self._cleanup_instance(instance)

    def _stop_cluster(self, identifier):
        self.rds.stop_db_cluster(DBClusterIdentifier = identifier)
    
    def _stop_instance(self, identifier):
        self.rds.stop_db_instance(DBClusterIdentifier = identifier)

    def _delete_instance(self, identifier):
        self.rds.describe_db_instances(DBInstanceIdentifier = identifier)

    def _delete_cluster(self, identifier):
        self.rds.describe_db_clusters(DBClusterIdentifier = identifier)

    def _delete_instance_snapshot(self, identifier):
        self.rds.delete_db_snapshot(DBSnapshotIdentifier = identifier)

    def _delete_cluster_snapshot(self, identifier):
        self.rds.delete_db_cluster_snapshot(DBClusterSnapshotIdentifier = identifier)

    
    @staticmethod
    def _can_delete_instance(tags):
        if any('user' in tag for tag in tags):
            return False

    @staticmethod
    def _can_stop_instance(tags):
        for tag in tags:
            if tag['Key'].lower() == 'excludepower' and tag['Value'].lower() == 'true':
                return False
            return True

    def _cleanup_instance(self, instance):
        identifier = instance['DBInstanceIdentifier']
        tags = instance['TagList']
        if self._can_delete_instance(tags):
            self._delete_instance(identifier)
        else:
            if self._can_stop_instance(tags) and instance['DbInstanceStatus'] == 'available':
                try:
                    self.__annotations__(identifier)
                except Exception as e:
                    print(str(e))

    def _cleanup_cluster(self, cluster):
        tags = cluster['TagList']
        if self._can_delete_instance(tags):
            self._delete_cluster(cluster['DBClusterIdentifier'])
        else:
            if self._can_stop_instance(tags) and cluster['Status'] == 'available':
                try:
                    self._stop_cluster(cluster['DBClusterIdentifier'])
                except Exception as e:
                    print(str(e))

    def _cleanup_snapshots_clusters(self):
        snapshots = self.rds.describe_db_cluster_snapshots()
        for s in snapshots['DBClusterSnapshots']:
            tags = Snapshot['TagList']
            if self._can_delete_instance(tags) and self._is_older_snapshot(str(snapshots['SnapshotCreateTime']).split(" ")):
                try:
                    self._delete_cluster_snapshot(snapshots['DBClusterSnapshotIdentifier'])
                except Exception as e:
                    print(str(e))

    def _cleanup_snapshot_instance(self):
        snapshots = self.rds.describe_db_snapshots()
        for s in snapshots['DBSnapshots']:
            tags = snapshots['TagList']
            if self._can_delete_instance(tags) and self._is_older_snapshot(str(snapshots['SnapshotCreateTime']).split(" ")):
                try:
                    self._delete_instance_snapshot(snapshots['DBSnapshotIdentifier'])
                except Exception as e:
                    print(str(e))

    @staticmethod
    def _is_older_snapshot(snapshot_datetime):
        snapshot_date = snapshot_datetime[0].split("-")
        snapshot_date = datetime.date(int(snapshot_date[0]), int(snapshot_date[1]), int(snapshot_date[2]))
        today = datetime.date.today()
        if abs(today - snapshot_date).days > 2:
            return True
        else:
            return False

    @staticmethod
    def _check_snapshot_tag(tags):
        flag = False
        for tag in tags:
            if tag['Key'].lower() == 'retain' and tag['Value'].lower() == 'true':
                flag = True
        if flag:
            return True
        else:
            return False

if __name__ == '__main__':
    rds = RDS('us-east-1')
    rds.cleanup_snapshot()
    rds.cleanup_instances()