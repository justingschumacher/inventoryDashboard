class InventoryDBRouter:
    """
    A router to control all inventory db requests.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'inventoryDashboard':
            return 'vmware_guest'
        return None