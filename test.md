
# Guidelines for writing clean python code

## Use type hints consistently
Use type hints for all function parameters and return values.

## Leverage Pydantic for data validation
Use Pydantic models to define and validate data structures.

## Follow PEP 8 style guidelines 
Use 4 spaces for indentation.
Limit lines to 79 characters.
Use snake_case for variable and function names.
Use CamelCase for class names.

## Write descriptive variable names
Choose clear and meaningful names for variables, functions, and classes.

## Use docstrings for documentation
Add docstrings to all functions, classes, and modules.

## Avoid magic numbers
Define constants for numeric values used in code.

## Handle exceptions properly
Use try/except blocks to handle exceptions gracefully.

## Keep functions small and focused
Each function should do one thing well.

## Use list comprehensions judiciously
Use list comprehensions for simple operations, but avoid complex nested ones.

## Leverage Pydantic's features
Use Field for additional validation.
Use Config classes to customize model behavior.
Use validators for complex validation logic.

## Write modular code
Break code into logical modules and packages.

## Use type aliases for complex types
Define type aliases for complex types to improve readability.

## Utilize Pydantic's built-in types
Use Pydantic's specialized types like EmailStr, HttpUrl, etc. when appropriate.

## Keep models separate from business logic
Define Pydantic models in separate files from business logic.

## Use enums for predefined sets of values
Define enums for sets of related constants.

## Implement custom validators when needed
Use Pydantic's validator decorators for complex field validation.

## Leverage Pydantic's config options
Use config options like allow_population_by_field_name for flexibility.

## Use abstract base classes when appropriate
Define abstract base classes for common interfaces.

## Follow the Single Responsibility Principle
Each class should have a single, well-defined purpose.

## Use type-safe equality comparisons
Use isinstance() for type checking instead of type().

## Leverage Pydantic's parsing functions
Use parse_obj_as and parse_file_as for flexible parsing.

## Keep models immutable when possible
Use frozen=True in Config to create immutable models.

## Use proper naming conventions for private attributes
Prefix private attributes with a single underscore.

## Utilize Pydantic's export functions
Use model_dump() and model_dump_json() for serialization.

## Follow consistent import style
Group imports: standard library, third-party, local.

## Use type unions for fields that can have multiple types
Use Union[Type1, Type2] for fields that can be of multiple types.

## Leverage Pydantic's alias feature
Use alias in Field for JSON keys that are not valid Python identifiers.

## Use proper type annotations for collections
Use List[Type], Dict[KeyType, ValueType], etc. for collections.

## Implement __str__ and __repr__ methods
Provide meaningful string representations for custom classes.

## Use dataclasses for simple data containers
Consider using dataclasses for simple data structures without validation.

## Leverage Pydantic's discriminated unions
Use discriminated unions for polymorphic models.

## Use context managers for resource management
Use 'with' statements for managing resources like file handles.

## Implement custom root validators when needed
Use root_validator for validations that involve multiple fields.

## Use proper type annotations for optional fields
Use Optional[Type] for fields that can be None.

## Leverage Pydantic's json_encoders
Define custom JSON encoders for complex types.

## Use proper type annotations for callable fields
Use Callable[[ArgType], ReturnType] for function fields.

## Implement custom error handling
Use Pydantic's ValidationError for detailed error messages.

