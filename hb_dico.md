# Dictionnaire de Données

## Table: factories
| Code       | Description          | Nature            | Contraintes             | Règle de Calcul |
|------------|----------------------|-------------------|-------------------------|-----------------|
| factory_id | Identifiant de l'usine | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| factory_name | Nom de l'usine        | Chaîne de caractères | Non nul                | N/A             |

## Table: employees
| Code        | Description          | Nature            | Contraintes             | Règle de Calcul |
|-------------|----------------------|-------------------|-------------------------|-----------------|
| employee_id | Identifiant de l'employé | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| firstname   | Prénom de l'employé   | Chaîne de caractères | Non nul                | N/A             |
| lastname    | Nom de famille de l'employé | Chaîne de caractères | Non nul                | N/A             |
| age         | Âge de l'employé      | Nombre entier     | Optionnel               | N/A             |
| start_date  | Date de début        | Date              | Non nul                | N/A             |
| end_date    | Date de fin          | Date              | Optionnel               | N/A             |
| is_active   | Actif (présent)      | Booléen           | Non nul, défaut TRUE    | N/A             |
| factory_id  | Identifiant de l'usine | Nombre entier     | Clé étrangère, référence factories(factory_id) | N/A             |

## Table: suppliers
| Code        | Description           | Nature            | Contraintes             | Règle de Calcul |
|-------------|-----------------------|-------------------|-------------------------|-----------------|
| supplier_id | Identifiant du fournisseur | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| supplier_name | Nom du fournisseur    | Chaîne de caractères | Non nul                | N/A             |

## Table: deliveries
| Code        | Description            | Nature            | Contraintes             | Règle de Calcul |
|-------------|------------------------|-------------------|-------------------------|-----------------|
| delivery_id | Identifiant de la livraison | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| supplier_id | Identifiant du fournisseur | Nombre entier     | Clé étrangère, référence suppliers(supplier_id) | N/A             |
| delivery_date | Date de livraison     | Date              | Non nul                | N/A             |
| quantity    | Quantité livrée        | Nombre entier     | Non nul                | N/A             |
| received_by | Identifiant de l'employé qui a réceptionné | Nombre entier | Clé étrangère, référence employees(employee_id), optionnel | N/A |
| factory_id  | Identifiant de l'usine  | Nombre entier     | Clé étrangère, référence factories(factory_id) | N/A             |

## Table: robots
| Code        | Description            | Nature            | Contraintes             | Règle de Calcul |
|-------------|------------------------|-------------------|-------------------------|-----------------|
| robot_id    | Identifiant du robot   | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| robot_model | Modèle du robot        | Chaîne de caractères | Non nul                | N/A             |
| produced_quantity | Quantité produite | Nombre entier     | Non nul                | N/A             |
| parts_used  | Pièces utilisées       | Nombre entier     | Non nul                | N/A             |
| factory_id  | Identifiant de l'usine | Nombre entier     | Clé étrangère, référence factories(factory_id) | N/A             |

## Table: audit_robot
| Code        | Description            | Nature            | Contraintes             | Règle de Calcul |
|-------------|------------------------|-------------------|-------------------------|-----------------|
| audit_id    | Identifiant de l'audit | Nombre entier     | Clé primaire, auto-incrément | N/A             |
| robot_id    | Identifiant du robot   | Nombre entier     | Clé étrangère, référence robots(robot_id) | N/A             |
| creation_date | Date de création     | Date              | Non nul, défaut CURRENT_DATE | N/A             |
